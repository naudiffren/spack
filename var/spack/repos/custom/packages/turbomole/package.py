from spack import *
import os
import subprocess

class Turbomole(Package):
    """TURBOMOLE: Program Package for ab initio Electronic Structure Calculations
       
       Note: Turbomole requires purchase of a license to download. Go to the
       Turbomole home page, http://www.turbomole-gmbh.com, for details. Spack
       will search the current directory for this file. It is probably best to
       add this file to a Spack mirror so that it can be found from anywhere.
       For information on setting up a Spack mirror see
       http://software.llnl.gov/spack/mirrors.html"""

    homepage = "http://www.turbomole-gmbh.com/"

    version('7.0.2', '92b97e1e52e8dcf02a4d9ac0147c09d6', url="file://%s/turbolinux702.tar.gz" % os.getcwd())

    variant('mpi', default=False, description='Set up MPI environment')
    variant('smp', default=False, description='Set up SMP environment')

    # Turbomole's install is odd. There are three variants
    # - serial
    # - parallel, MPI
    # - parallel, SMP
    #
    # Only one of these can be active at a time. MPI and SMP are set as
    # variants so there could be up to 3 installs per version. Switching
    # between them would be accomplished with `module swap` commands. 

    def install(self, spec, prefix):
        if spec.satisfies('@:7.0.2'):
            calculate_version = 'calculate_2.4_linux64'
            molecontrol_version = 'MoleControl_2.5'

        if '+mpi' in spec and '+smp' in spec:
	    raise InstallError('Can not have both SMP and MPI enabled in the same build.')
        tar = which('tar')
	dst = join_path(prefix, 'TURBOMOLE')

        tar('-x', '-z', '-f', 'thermocalc.tar.gz')
        with working_dir('thermocalc'):
            cmd = 'sh install <<<y'
            subprocess.call(cmd, shell=True)

        install_tree('basen', join_path(dst, 'basen'))
        install_tree('cabasen', join_path(dst, 'cabasen'))
        install_tree(calculate_version, join_path(dst, calculate_version))
        install_tree('cbasen', join_path(dst, 'cbasen'))
        install_tree('DOC', join_path(dst, 'DOC'))
        install_tree('jbasen', join_path(dst, 'jbasen'))
        install_tree('jkbasen', join_path(dst, 'jkbasen'))
        install_tree('libso', join_path(dst, 'libso'))
        install_tree(molecontrol_version, join_path(dst, molecontrol_version))
        install_tree('mpirun_scripts', join_path(dst, 'mpirun_scripts'))
        install_tree('parameter', join_path(dst, 'parameter'))
        install_tree('perlmodules', join_path(dst, 'perlmodules'))
        install_tree('scripts', join_path(dst, 'scripts'))
        install_tree('smprun_scripts', join_path(dst, 'smprun_scripts'))
        install_tree('structures', join_path(dst, 'structures'))
        install_tree('thermocalc', join_path(dst, 'thermocalc'))
        install_tree('TURBOTEST', join_path(dst, 'TURBOTEST'))
        install_tree('xbasen', join_path(dst, 'xbasen'))

        install('Config_turbo_env', dst)
        install('Config_turbo_env.tcsh', dst)
        install('README', dst)
        install('README_LICENSES', dst)
        install('TURBOMOLE_702_LinuxPC', dst)

	if '+mpi' in spec:
	    install_tree('bin/x86_64-unknown-linux-gnu_mpi', join_path(dst, 'bin', 'x86_64-unknown-linux-gnu_mpi'))
	elif '+smp' in spec:
	    install_tree('bin/x86_64-unknown-linux-gnu_smp', join_path(dst, 'bin', 'x86_64-unknown-linux-gnu_smp'))
        else:
	    install_tree('bin/x86_64-unknown-linux-gnu', join_path(dst, 'bin', 'x86_64-unknown-linux-gnu'))

    def setup_environment(self, spack_env, run_env):
        if self.spec.satisfies('@:7.0.2'):
            molecontrol_version = 'MoleControl_2.5'

        run_env.set('TURBODIR', join_path(self.prefix, 'TURBOMOLE'))
	run_env.set('MOLE_CONTROL', join_path(self.prefix, 'TURBOMOLE', molecontrol_version))

	run_env.prepend_path('PATH', join_path(self.prefix, 'TURBOMOLE', 'thermocalc'))
	run_env.prepend_path('PATH', join_path(self.prefix, 'TURBOMOLE', 'scripts'))
        if '+mpi' in self.spec:
            run_env.set('PARA_ARCH', 'MPI')
            run_env.prepend_path('PATH', join_path(self.prefix, 'TURBOMOLE', 'bin', 'x86_64-unknown-linux-gnu_mpi'))
        elif '+smp' in self.spec:
            run_env.set('PARA_ARCH', 'SMP')
            run_env.prepend_path('PATH', join_path(self.prefix, 'TURBOMOLE', 'bin', 'x86_64-unknown-linux-gnu_smp'))
        else:
            run_env.prepend_path('PATH', join_path(self.prefix, 'TURBOMOLE', 'bin', 'x86_64-unknown-linux-gnu'))

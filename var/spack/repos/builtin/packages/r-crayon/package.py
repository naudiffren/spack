##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class RCrayon(Package):
    """Colored terminal output on terminals that support 'ANSI' color and
    highlight codes. It also works in 'Emacs' 'ESS'. 'ANSI' color support is
    automatically detected. Colors and highlighting can be combined and nested.
    New styles can also be created easily. This package was inspired by the
    'chalk' 'JavaScript' project."""

    homepage = "https://github.com/gaborcsardi/crayon"
    url = "https://cran.r-project.org/src/contrib/crayon_1.3.1.tar.gz"

    version('1.3.1', 'a013b6fe8931374fe40261a6bbefe1ba')

    extends('R')

    depends_on('r-memoise')

    def install(self, spec, prefix):
        R('CMD', 'INSTALL', '--library={0}'.format(self.module.r_lib_dir),
          self.stage.source_path)

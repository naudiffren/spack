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


class RRbenchmark(Package):
    """rbenchmark is inspired by the Perl module Benchmark, and is intended to
    facilitate benchmarking of arbitrary R code. The library consists of just
    one function, benchmark, which is a simple wrapper around system.time.
    Given a specification of the benchmarking process (counts of replications,
    evaluation environment) and an arbitrary number of expressions, benchmark
    evaluates each of the expressions in the specified environment, replicating
    the evaluation as many times as specified, and returning the results
    conveniently wrapped into a data frame."""

    homepage = "http://rbenchmark.googlecode.com/"
    url = "https://cran.r-project.org/src/contrib/rbenchmark_1.0.0.tar.gz"

    version('1.0.0', 'e8fe50e0eebc3330d1fbe1c54678bf9f')

    extends('R')

    def install(self, spec, prefix):
        R('CMD', 'INSTALL', '--library={0}'.format(self.module.r_lib_dir),
          self.stage.source_path)

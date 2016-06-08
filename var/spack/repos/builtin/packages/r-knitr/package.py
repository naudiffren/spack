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


class RKnitr(Package):
    """Provides a general-purpose tool for dynamic report generation in R using
    Literate Programming techniques."""

    homepage = "http://yihui.name/knitr/"
    url = "https://cran.r-project.org/src/contrib/knitr_1.13.tar.gz"

    version('1.13', 'a9960a644fa30bc33505f3c5f176ca18')

    extends('R')

    depends_on('r-evaluate')
    depends_on('r-digest')
    depends_on('r-formatR')
    depends_on('r-highr')
    depends_on('r-markdown')
    depends_on('r-stringr')
    depends_on('r-yaml')

    def install(self, spec, prefix):
        R('CMD', 'INSTALL', '--library={0}'.format(self.module.r_lib_dir),
          self.stage.source_path)

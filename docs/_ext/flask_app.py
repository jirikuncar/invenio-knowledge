# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Check application context for Sphinx build."""


def setup(sphinx):
    """Setup Sphinx object."""
    from flask import has_app_context
    from invenio.base.factory import create_app
    PACKAGES = ['invenio.base', 'invenio.modules.accounts',
                'invenio.modules.records', 'invenio_knowledge']

    if not has_app_context():
        app = create_app(PACKAGES=PACKAGES)
        ctx = app.test_request_context('/')
        ctx.push()

# -*- coding: utf-8 -*-

import os
import glob
import logging

from zope.interface import Interface

from zope.configuration.fields import Path
logger = logging.getLogger('tomcom.plone.ptregistry')

from Products.Five.browser.metaconfigure import page

class IPTDirective(Interface):
    """ZCML directive to register a directory as a directory wich holds templates.
    """

    path = Path(
        title=u"Path to the directory.",
        description=u"""The registry is for public templates only.""",
        required=True
        )

def register(_context, path):
    """ZCML directive handler"""

    if os.path.exists(path):
        for file_name in glob.glob(path+os.sep+'*.pt'):
            page(_context,
                 file_name.split(os.sep)[-1][:-3],
                 'zope2.View',
                 None,
                 template=file_name
                 )
    else:
        logger.error('PATH does not exist: %s'%path)

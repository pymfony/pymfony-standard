#!python
# -*- coding: utf-8 -*-

import sys;

from pymfony.component.console import Request;
from app_kernel import AppKernel;

kernel = AppKernel("dev", True);

request = Request.createFromGlobals();
response = kernel.getCliKernel().handle(request);
response.send();

sys.exit(response.getStatusCode());

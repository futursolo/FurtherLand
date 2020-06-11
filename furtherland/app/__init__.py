#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   Copyright 2020 Kaede Hoshikawa
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from __future__ import annotations
from typing import Dict, Any

from ..utils import flatten_async

from .common import FurtherLand

from . import signin

import hakoniwa

__all__ = ["FurtherLand"]

_land = FurtherLand.get()

_land.app.handlers.add(
    hakoniwa.ReRule(r"^signin$", signin.SignInHandler), name="signin")

_land.app.handlers.add(
    hakoniwa.ReRule(r"^signup$", signin.SignUpHandler), name="signup")


@flatten_async
async def process_lambda_request(
        event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    return await _land.process_lambda_request(event)

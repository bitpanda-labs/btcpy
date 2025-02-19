# Copyright (C) 2017 chainside srl
#
# This file is part of the btcpy package.
#
# It is subject to the license terms in the LICENSE.md file found in the top-level
# directory of this distribution.
#
# No part of btcpy, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE.md file.
import threading

__all__ = ['utils',
           'ds']
#  btcpy has a state which can change in a multithreaded environment
#  this lock can be used to prevent possible race conditions
lock = threading.Lock()

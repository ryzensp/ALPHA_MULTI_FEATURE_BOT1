#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# MIT License
# Copyright (c) 2020 Stɑrry Shivɑm // This file is part of AcuteBot
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os, sys, logging
from functools import wraps
from telegram.ext import Updater, Defaults

    TOKEN = os.environ.get("TOKEN")
    WORKERS = int(os.environ.get("WORKERS", 8))
    TMDBAPI = os.environ.get("TMDBAPI")
    DB_URI = os.environ.get("DATABASE_URL")
    GENIUS = os.environ.get("GENIUS")
    DEBUG = bool(os.environ.get("DEBUG", False)) 
    APIID = os.environ.get("APIID")
    APIHASH = os.environ.get("APIHASH")



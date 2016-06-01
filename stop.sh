#!/usr/bin/env bash
kill -9 `ps aux | grep weblogprovws | grep -v grep | awk '{print \$2}'`
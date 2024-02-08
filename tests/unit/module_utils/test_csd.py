# -*- coding: utf-8 -*-

# (c) Copyright IBM Corp. 2023
# Apache License, Version 2.0 (see https://opensource.org/licenses/Apache-2.0)

from __future__ import absolute_import, division, print_function
from ansible_collections.ibm.ibm_zos_cics.plugins.module_utils.response import _execution
from ansible_collections.ibm.ibm_zos_cics.tests.unit.helpers.data_set_helper import PYTHON_LANGUAGE_FEATURES_MESSAGE, CSDUP_name, CSDUP_stderr, CSDUP_stdout

from ansible_collections.ibm.ibm_zos_core.plugins.module_utils.zos_mvs_raw import MVSCmdResponse

__metaclass__ = type
from ansible_collections.ibm.ibm_zos_cics.plugins.module_utils import csd
from ansible_collections.ibm.ibm_zos_cics.plugins.module_utils import dataset_utils
import pytest
import sys

try:
    from unittest.mock import MagicMock
except ImportError:
    from mock import MagicMock


NAME = "ANSI.TEST.DFHCSD"


@pytest.mark.skipif(sys.version_info.major < 3, reason=PYTHON_LANGUAGE_FEATURES_MESSAGE)
def test_get_idcams_cmd_megabytes():
    csd_data_set = dict(
        name=NAME,
        sdfhload="CICSTS.IN56.SDFHLOAD",
        state="initial",
        exists=False,
        data_set_organization="NONE",
        unit="M",
        primary=3,
        secondary=1
    )
    idcams_cmd_csd = dataset_utils._build_idcams_define_cmd(csd._get_idcams_cmd_csd(csd_data_set))
    assert idcams_cmd_csd == '''
    DEFINE CLUSTER (NAME(ANSI.TEST.DFHCSD) -
    MEGABYTES(3 1) -
    RECORDSIZE(200 2000) -
    INDEXED -
    KEYS(22 0) -
    FREESPACE(10 10) -
    SHAREOPTIONS(2) -
    REUSE) -
    DATA (NAME(ANSI.TEST.DFHCSD.DATA) -
    CONTROLINTERVALSIZE(8192)) -
    INDEX (NAME(ANSI.TEST.DFHCSD.INDEX))
    '''


@pytest.mark.skipif(sys.version_info.major < 3, reason=PYTHON_LANGUAGE_FEATURES_MESSAGE)
def test_get_idcams_cmd_cylinders():
    csd_data_set = dict(
        name=NAME,
        sdfhload="CICSTS.IN56.SDFHLOAD",
        state="initial",
        exists=False,
        data_set_organization="NONE",
        unit="CYL",
        primary=3,
        secondary=1
    )
    idcams_cmd_csd = dataset_utils._build_idcams_define_cmd(csd._get_idcams_cmd_csd(csd_data_set))
    assert idcams_cmd_csd == '''
    DEFINE CLUSTER (NAME(ANSI.TEST.DFHCSD) -
    CYLINDERS(3 1) -
    RECORDSIZE(200 2000) -
    INDEXED -
    KEYS(22 0) -
    FREESPACE(10 10) -
    SHAREOPTIONS(2) -
    REUSE) -
    DATA (NAME(ANSI.TEST.DFHCSD.DATA) -
    CONTROLINTERVALSIZE(8192)) -
    INDEX (NAME(ANSI.TEST.DFHCSD.INDEX))
    '''


def test_csdup_response():
    csd_input = {
        "exists": False,
        "name": NAME,
        "primary": 5,
        "secondary": 1,
        "unit": "M",
        "state": "initial",
        "vsam": False,
        "sdfhload": "CICSTS.IN56.SDFHLOAD",
    }

    expected_executions = [
        _execution(name=CSDUP_name(), rc=0, stdout=CSDUP_stdout(NAME), stderr=CSDUP_stderr(NAME)),
    ]

    csd._execute_dfhcsdup = MagicMock(return_value=MVSCmdResponse(rc=0, stdout=CSDUP_stdout(NAME), stderr=CSDUP_stderr(NAME)))
    executions = csd._run_dfhcsdup(csd_input)

    assert executions == expected_executions


def test_bad_csdup_response():
    csd_input = {
        "exists": False,
        "name": NAME,
        "primary": 5,
        "secondary": 1,
        "unit": "M",
        "state": "initial",
        "vsam": False,
        "sdfhload": "CICSTS.IN56.SDFHLOAD",
    }

    expected_executions = [
        _execution(name=CSDUP_name(), rc=99, stdout=CSDUP_stdout(NAME), stderr=CSDUP_stderr(NAME)),
    ]

    csd._execute_dfhcsdup = MagicMock(return_value=MVSCmdResponse(rc=99, stdout=CSDUP_stdout(NAME), stderr=CSDUP_stderr(NAME)))

    try:
        csd._run_dfhcsdup(csd_input)
    except Exception as e:
        error_message = e.args[0]
        executions = e.args[1]

        assert error_message == "DFHCSDUP failed with RC 99"
        assert executions == expected_executions

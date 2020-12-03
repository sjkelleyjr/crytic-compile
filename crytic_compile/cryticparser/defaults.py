"""
Default value for options
"""
# Those are the flags shared by the command line and the config file
DEFAULTS_FLAG_IN_CONFIG = {
    "compile_force_framework": None,
    "compile_remove_metadata": False,
    "compile_custom_build": None,
    "solc": "solc",
    "solc_remaps": None,
    "solc_args": None,
    "solc_disable_warnings": False,
    "solc_working_dir": None,
    "solc_solcs_select": None,
    "solc_solcs_bin": None,
    "solc_standard_json": False,
    "solc_force_legacy_json": False,
    "truffle_version": None,
    "truffle_ignore_compile": False,
    "truffle_build_directory": "build/contracts",
    "truffle_overwrite_config": False,
    "truffle_overwrite_version": None,
    "embark_ignore_compile": False,
    "embark_overwrite_config": False,
    "brownie_ignore_compile": False,
    "dapp_ignore_compile": False,
    "etherlime_ignore_compile": False,
    "etherlime_compile_arguments": None,
    "etherscan_only_source_code": False,
    "etherscan_only_bytecode": False,
    "etherscan_api_key": None,
    "waffle_ignore_compile": False,
    "waffle_config_file": None,
    "npx_disable": False,
    "ignore_compile": False,
    "buidler_ignore_compile": False,
    "buidler_cache_directory": "cache",
    "buidler_skip_directory_name_fix": False,
    "hardhat_ignore_compile": False,
    "hardhat_cache_directory": "cache",
    "hardhat_artifacts_directory": "artifacts",
}

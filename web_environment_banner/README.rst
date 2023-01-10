======================
web_environment_banner
======================

When the configuration file has something like the following set: ::

    [web_environment_banner]
    enabled = true
    name = DEVELOPMENT: {hostname}

An obvious banner is placed across the top of the frontend, backend, and
web/database/manager.

If the configuration is not enabled, then nothing happens.

This module was inspired by the OCA/web/web_environment_banner module, however
this moves it "up the stack" allowing it to function based on the
instance/server level rather than the database level.

This module is intended to be used as a server_wide_module.


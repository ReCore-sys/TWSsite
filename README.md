
# TWSsite

This is repository of tws official web site. Site servs informative role but also provides some functionality
as testing, login and transactions.

## internals

Site is hosted from same host as server. The configurations of each game server is accessed trough environment
variables, to access public configuration details that are also available trough game commands. The web is also connected
and reads and modifies database as needed.

"""
Invoke commands to be run inside the backend container
"""

import invoke

import net.invoke.sundry
import net.invoke.tests


# Default invoke collection
ns = invoke.Collection()

# Add collections defined in other files
ns.add_collection(net.invoke.sundry)
ns.add_collection(net.invoke.tests)

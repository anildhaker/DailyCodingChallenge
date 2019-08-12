# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".


def defangIPaddr(address):
      x = address.split('.')
      y='[.]'.join(x)
      return y
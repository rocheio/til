# Restore SSH Key from Keepass

*from [Rick Benetti on StackOverflow](http://stackoverflow.com/a/37779390)*

When restoring a computer, you might need to migrate SSH access from a machine you no longer have access to. Hopefully you've saved these SSH keys in an encrypted storage program like [Keepass](http://keepass.info/).

Copy the text of the SSH private / public keys to files on the new machine, and then use the following command to allow them to be read by the filesystem.

```bash
chmod 400 ~/.ssh/id_rsa_old
```

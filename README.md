# Ipnotify

*ipnotify* is a small utility which queries external tools, gets the IP address of the host it is runing on, and sends notification, if the IP address is changed since the last execution.

## Installation
To install *ipnotify* just run `install.sh`.

### Directories
By default the installer will install the application to `/opt/ipnotify`

    /opt/ipnotify
    |
    +---- data
    | +---- db.sqlite3      (SQLite database, public ip addresses history)
    |
    +--- etc
    | +---- ipnotify.conf   (main configuration file)
    | +---- logging.conf    (logging configuration file)
    |
    +---- ipnotify          (Python sources)
    |
    +---- log
      +---- ipnotify.log    (log file)

## Configuration
Before running *ipnotify* for the first time you might want to configure it, in order to run it properly.

Edit `/opt/ipnotify/etc/ipnotify.conf` *email* stanza:


    [email]
    # email subject
    subject: ipnotify
    # sender's email
    sender: root@localhost
    # recipipents separated by commas
    recipients: root@localhost

set recipients, and the other parameters to suit your needs.

You might also want to configure `SMTP` stanza, in case your *MTA* cannot send e-mails over the Internet.

## Uninstallation
To uninstall *ipnotify* just run `uninstall.sh`.
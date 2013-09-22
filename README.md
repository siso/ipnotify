# Ipnotify

*ipnotify* queries external services, gets public IP address, and sends notification if it is changed since last execution.

## Installation
Get the sources:

```git clone https://github.com/siso/ipnotify```

and install it:

```
cd ipnotify
python setup.py install
```

### Files and directories

    ~/.ipnotify/db.sqlite3          SQLite database, public ip addresses history
    ~/.ipnotify/ipnotify.conf       main configuration file
    ~/.ipnotify/logging.conf        logging configuration file
    ~/.ipnotify/ipnotify.log        log file

## Configuration
Before running *ipnotify* for the first time you might want to configure it, in order to run it properly.

Edit *email* stanza in ```~/.ipnotify/ipnotify.conf```:

    [email]
    # email subject
    subject: ipnotify
    # sender's email
    sender: root@localhost
    # recipipents separated by commas
    recipients: root@localhost

set recipients, and the other parameters to suit your needs.

You might also want to configure `SMTP` stanza, in case your *MTA* cannot send e-mails over the Internet.

## Credits
ipnotify  is  written  and  maintained  by  Simone  Soldateschi   (simone.soldateschi@gmail.com).  If you have any questions, comments, suggestions or concerns, please let  me  know  or  post  them  to  https://github.com/siso/ipnotify/issues.


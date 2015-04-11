import sublime, sublime_plugin
import os
import datetime
import random
import getpass

''' Add license stamp
/**
* @version   $Id: ${1:current_file_name.extension} ${2:random_4_digit_number} ${3:YYYY-MM-DD} ${4:time_in_UTC_24} ${5:current_logged-in_user} $
* @author    Company http://example.com
* @copyright Copyright (C) 2007 - ${6:current_year} Company
* @license   http://www.gnu.org/licenses/gpl-2.0.html GNU/GPLv2 only
*/
'''


class AddLicenseStampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        company_name = "Raphael.Syed <raphael.syed@WhereGroup.com>"
        company_site = "http://WhereGroup.com"

        file_path = self.view.file_name()
        file_name = os.path.basename(file_path)
        year = datetime.datetime.utcnow().strftime("%Y")
        date_time = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
        random_number = str(random.randrange(0000, 9999)).zfill(4)
        user = getpass.getuser()

        license = "/**\n"
        license += " * @version   Changed: ### " + date_time + " ###"  "\n"
        license += " * @author    " + company_name + " " + company_site + "\n"
        # license += "* @copyright Copyright (C) 2015 - " + year + " " + company_name + "\n"
        # license += "* @license   http://www.gnu.org/licenses/gpl-2.0.html GNU/GPLv2 only\n"
        license += " */\n"

        # license = "/**\n"
        # license += "* @version   $Id: " + file_name + " " + random_number + " " + date_time + " " + user + " $\n"
        # license += "* @author    " + company_name + " " + company_site + "\n"
        # # license += "* @copyright Copyright (C) 2015 - " + year + " " + company_name + "\n"
        # # license += "* @license   http://www.gnu.org/licenses/gpl-2.0.html GNU/GPLv2 only\n"
        # license += "*/\n"

        self.view.replace(edit, self.view.sel()[0], license)

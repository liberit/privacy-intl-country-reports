#!/usr/bin/env python

# -*- coding: utf-8 -*-
#    This file is part of liberit.

#    liberit is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    liberit is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with liberit.  If not, see <http://www.gnu.org/licenses/>.

# (C) 2012 Stefan Marsiske <s@ctrlc.hu>


from urlparse import urljoin

base="https://www.privacyinternational.org/projects/global-country-reports"

from scraptils.utils import jdump, getFrag

def scrape():
    for countrya in getFrag(base, '//ul[@class="country-reports-list"]/li/a'):
        url=urljoin(base ,countrya.get('href'))
        country=countrya.xpath('text()')[0]
        for chapter in getFrag(url, '//div[@class="book-navigation"]/ul[@class="menu"]//a'):
            print jdump({'country': country,
                         'url': urljoin(base ,chapter.get('href')),
                         'chapter': chapter.xpath('text()')[0].split(' ',1)[1]
                         }).encode('utf8').replace('\n','')
scrape()

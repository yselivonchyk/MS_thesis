########################################################################
# Autonomous Intelligent System, University of Bonn, LaTeX Beamer theme
# 
# Copyright (C) 2010-2013 Dirk Holz, dirk.holz@ieee.org
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#!/usr/bin/make -f

MAINSRC = presentation

all:	
	rubber --pdf -I . -I style --force $(MAINSRC)

clean:	
	rm -f *.aux *.bbl *.blg *.log *.lof *.log *.lot *.out *.toc *.synctex.gz *.snm *.nav *~ $(MAINSRC).dvi $(MAINSRC).ps $(MAINSRC).pdf

tarball: clean
	tar czvf ../$(MAINSRC).tgz --exclude-vcs --exclude-backups --exclude=$(MAINSRC).tgz .

gitignore:
	@echo "*.aux\n*.bbl\n*.blg\n*.log\n*.lof\n*.log\n*.lot\n*.out\n*.toc\n*.synctex.gz\n*.snm\n*.nav\n*~\n$(MAINSRC).dvi\n$(MAINSRC).ps\n$(MAINSRC).pdf" >> .gitignore
	git add .gitignore

svnignore:
	@echo "*.aux\n*.bbl\n*.blg\n*.log\n*.lof\n*.log\n*.lot\n*.out\n*.toc\n*.synctex.gz\n*.snm\n*.nav\n*~\n$(MAINSRC).dvi\n$(MAINSRC).ps\n$(MAINSRC).pdf" | svn propset svn:ignore . -RF -

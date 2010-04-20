Summary:	jQuery.spritely plugin
Name:		jquery-spritely
Version:	0.2.1
Release:	0.3
License:	MIT / GPL v2
Group:		Applications/WWW
Source0:	http://www.spritely.net/lib/jquery/1.3.2/plugins/jquery.spritely-%{version}.js
# Source0-md5:	3eed51a17d30bc6594ab350c84be2a38
Source1:	http://www.spritely.net/usr/library/documents/sample-code/spritely-0.2-sample-code.zip
# Source1-md5:	096ea7501f24a302cda8f4c0c4d1b0b3
URL:		http://www.spritely.net/
BuildRequires:	rpmbuild(macros) > 1.268
Requires:	jquery >= 1.3
# for graggable
Suggests:	jquery-ui
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/jquery

%description
jQuery.spritely is a jQuery plugin for creating dynamic character and
background animation in pure HTML and JavaScript. It's a simple,
light-weight plugin with a few simple methods for creating animated
sprites such as the birds you see on this page, and dynamic scrolling
backgrounds.

%package demo
Summary:	Demo for jQuery.spritely
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.spritely
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	js-sizzle
Requires:	jquery-ui

%description demo
Demonstrations and samples for jQuery.spritely.

%prep
%setup -qcT -a1
cp -a %{SOURCE0} jquery.spritely.js
mv spritely-0.2-sample-code sample-code

find '(' -name '*.js' -o -name '*.html' ')' -print0 | xargs -0 %{__sed} -i -e 's,\r$,,'

cd sample-code
ln -s %{_appdir}/jquery.js scripts
ln -s /usr/share/js-sizzle/sizzle.js scripts
ln -s %{_appdir}/jquery.spritely.js scripts
ln -s %{_appdir}/ui/ui.core.js scripts
ln -s %{_appdir}/ui/ui.draggable.js scripts
ln -s %{_appdir}/ui/ui.slider.js scripts

rm scripts/jquery-1.3.2.min.js
rm scripts/jquery-ui-1.7.2.spritely.custom.min.js
rm scripts/jquery.spritely-0.2.js

sed -i -e '
	s,scripts/jquery-1.3.2.min.js,scripts/jquery.js,
		/scripts\/jquery.js/a	<script src="scripts/sizzle.js" type="text/javascript"></script>

	s,scripts/jquery-ui-1.7.2.spritely.custom.min.js,scripts/ui.core.js,
		/scripts\/ui.core.js/a	<script src="scripts/ui.draggable.js" type="text/javascript"></script>
		/scripts\/ui.core.js/a	<script src="scripts/ui.slider.js" type="text/javascript"></script>

	s,scripts/jquery.spritely-0.2.js,scripts/jquery.spritely.js,
' index.html

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}
cp -a jquery.spritely.js $RPM_BUILD_ROOT%{_appdir}
cp -a sample-code/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}/jquery.spritely.js

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

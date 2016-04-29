#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-dm-active_model
Version  : 1.2.1
Release  : 5
URL      : https://rubygems.org/downloads/dm-active_model-1.2.1.gem
Source0  : https://rubygems.org/downloads/dm-active_model-1.2.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-dm-core
BuildRequires : rubygem-dm-validations
BuildRequires : rubygem-jeweler
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec

%description
= dm-active_model
This plugin makes datamapper compliant with active_model conventions and thus compatible with rails3.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n dm-active_model-1.2.1
gem spec %{SOURCE0} -l --ruby > rubygem-dm-active_model.gemspec

%build
gem build rubygem-dm-active_model.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
dm-active_model-1.2.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/dm-active_model-1.2.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/.document
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/CHANGELOG
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/TODO
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/VERSION
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/dm-active_model.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/lib/dm-active_model.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/lib/dm-active_model/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/spec/amo_interface_compliance_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/spec/amo_validation_compliance_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/spec/dm-active_model_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/spec/lib/amo_lint_extensions.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/spec/rcov.opts
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/spec/spec.opts
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/tasks/changelog.rake
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/tasks/spec.rake
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/tasks/yard.rake
/usr/lib64/ruby/gems/2.3.0/gems/dm-active_model-1.2.1/tasks/yardstick.rake
/usr/lib64/ruby/gems/2.3.0/specifications/dm-active_model-1.2.1.gemspec

"""
Copyright 2013 - CANARIE Inc. All rights reserved

Synopsis: Site URL configuration and routing

Blob Hash: $Id$

-------------------------------------------------------------------------------

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. The name of the author may not be used to endorse or promote products
   derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY CANARIE Inc. "AS IS" AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

from django.conf.urls import url

from canarie_service import views

app_name = 'canarie_service'

urlpatterns = [
  url(r'^info$', views.info, name='info'),
  url(r'^stats$', views.stats, name='stats'),
  url(r'^doc$', views.doc, name='doc'),
  url(r'^releasenotes$', views.release_notes, name='releasenotes'),
  url(r'^support$', views.support, name='support'),
  url(r'^source$', views.source, name='source'),
  url(r'^tryme$', views.app, name='tryme'),
  url(r'^licence$', views.licence, name='licence'),
  url(r'^provenance$', views.provenance, name='provenance'),
  url(r'^app$', views.app, name='app'),
  url(r'^update$', views.update, name='update'),
  url(r'^reset$', views.reset, name='reset'),
  url(r'^add$', views.add, name='add'),
  url(r'^setinfo$', views.setinfo, name='setinfo'),
]

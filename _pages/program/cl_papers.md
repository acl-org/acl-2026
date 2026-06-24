---
title: Accepted CL Papers
layout: single
excerpt: "Accepted CL Papers of ACL 2026"
permalink: /program/cl_papers/
sidebar:
  nav: "program"
---

{% for paper in site.data.papers_cl %}
  - **{{ paper.title }}**<br>*{{ paper.authors }}*
{% endfor %}

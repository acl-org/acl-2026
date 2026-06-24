---
title: Accepted CL Papers
layout: single
excerpt: "Accepted CL Papers of ACL 2026"
permalink: /program/cl_papers/
sidebar:
  nav: "program"
toc: True
toc_sticky: True
---

{% for paper in site.data.papers_cl %}
  - **{{ paper.title }}**<br>*{{ paper.authors }}*
{% endfor %}

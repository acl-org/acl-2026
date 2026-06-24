---
title: Accepted TACL Papers
layout: single
excerpt: "Accepted TACL Papers of ACL 2026"
permalink: /program/tacl_papers/
sidebar:
  nav: "program"
---

{% for paper in site.data.papers_tacl %}
  - **{{ paper.title }}**<br>*{{ paper.authors }}*
{% endfor %}

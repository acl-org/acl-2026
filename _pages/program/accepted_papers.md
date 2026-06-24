---
title: Accepted Main Conference Papers
layout: single
excerpt: "Accepted Main Conference Papers of ACL 2026"
permalink: /program/accepted_papers/
sidebar:
  nav: "program"
toc: True
toc_sticky: True
---

{% for paper in site.data.papers_main %}
  - **{{ paper.title }}**<br>*{{ paper.authors }}*
{% endfor %}

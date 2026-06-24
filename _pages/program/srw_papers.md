---
title: Accepted Student Research Workshop Papers
layout: single
excerpt: "Accepted Student Research Workshop Papers of ACL 2026"
permalink: /program/tacl_papers/
sidebar:
  nav: "program"
toc: True
toc_sticky: True
---

{% for paper in site.data.papers_srw %}
  - **{{ paper.title }}**<br>*{{ paper.authors }}*
{% endfor %}

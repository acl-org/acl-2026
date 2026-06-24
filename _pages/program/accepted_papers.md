---
title: Accepted Main Conference Papers
layout: single
excerpt: "Accepted Main Conference Papers of ACL 2026"
permalink: /program/accepted_papers/
sidebar:
  nav: "program"
---

{% for paper in site.data.papers_main %}
  - **{{ paper.title }}**<br>*{{ paper.authors }}*
{% endfor %}

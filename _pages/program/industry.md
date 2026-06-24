---
title: Accepted Industry Track Papers
layout: single
excerpt: "Accepted Industry Track Papers of ACL 2026"
permalink: /program/industry/
sidebar:
  nav: "program"
---

{% for paper in site.data.papers_industry %}
  - **{{ paper.title }}**<br>*{{ paper.authors }}*
{% endfor %}

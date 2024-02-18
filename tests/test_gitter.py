import sys
sys.path.append("..")

from gitter import gitter_meta

def test_get_octocat():
  octocat = gitter_meta.get_octocat()
  assert octocat["status"] == 200
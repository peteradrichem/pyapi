from npoapi.npoapi import NpoApi
import urllib.request


class Media(NpoApi):
    def get(self, mid):
        return self.request("/api/media/" + urllib.request.quote(mid))

    def list(self):
        return self.request("/api/media")

    def search(self, form="{}", sort="asc", offset=0, max_=240):
        return self.request("/api/media", data=form, params={"sort": sort, "offset": offset, "max": max_})

    def changes(self, profile=None, order="ASC"):
        return self.request("/api/media/changes", params={"profile": profile, "order": order, "max": 10})
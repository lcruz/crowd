from models import Offer
import appengine_admin

class OfferAdmin(appengine_admin.ModelAdmin):
    model = Offer
    listFields = ('title', 'description')
    editFields = ('title', 'description')
    readonlyFields = ('owner', 'date')

appengine_admin.register(OfferAdmin)
from dajax.core import Dajax

def getNextCountry(request, country_list):

    print >>sys.stderr, "hit"

    dajax = Dajax()
    country_list.pop[0]
    dajax.assign('#test', 'innerHTML',country_list)
    return dajax.json()
}

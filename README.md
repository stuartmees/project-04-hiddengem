# Hidden Gem
project-04

### Timeframe
7 days

## Technologies used

* React
* PostgreSQL
* Flask
* Pony ORM
* JavaScript (ES6)
* HTML5
* CSS
* Bulma
* Axios
* React Asyn Select
* ReactMapBox-GL
* Google Places API
* webpack
* git/GitHub
* Insomnia


### Introduction
My brief was to create a full-stack web app with a RESTful API. The API was to be made with a Flask app and a PostgreSQL database and it was to be consumed by a React front end.

My app is a website that enables users to register, log in and post details of 'hidden gems' (entries) they found and visited in India.

![image](https://user-images.githubusercontent.com/35113861/59159496-46f10580-8ac2-11e9-8b2b-90109e441eb9.png)


## Process
_Describe the process of building the game. How did you get started? How did you manage your time? How would you do things next time?_

Like I did previously I made wireframes that enabled me to ascertain what functionality I wanted the website to have. This furthermore guided the desgin om the PostgreSQL datbase.

The Flask App and database was the first thing to be created to enable entry and user info to be stored.

Once this API was in place, and all routes tested in Insomnia, the building of the React app could begin to consume our API.

### Web App Overview

A one page app was created that rendered different components depending on the path:

```      
<Router>
  <main>
    <Navbar />
    <FlashMessages />
    <Switch>
      <Route path="/entries/new" component={EntriesNew} />
      <Route path="/entries/:id" component={EntriesShow} />
      <Route path="/entries" component={EntriesIndex} />
      <Route path="/login" component={Login} />
      <Route path="/register" component={Register} />
      <Route path="/" component={Home} />
    </Switch>
  </main>
</Router>
```

The Navbar component renders on every route with conditional rendering determining which link in the component to display on the specific route.

All the entries in the database are shown on a map by markers places in the respective position on the Index component:

![image](https://user-images.githubusercontent.com/35113861/59159570-adc2ee80-8ac3-11e9-83d5-1332f3aa1c8f.png)

Users are able to search the database directly from the search bar in the home component and within the map Index component. Users can also filter the search results by category from a drop down menu from within the map Index component.

All the information within an entry is viewed in the Show component, which can be accessed by  clicking on the relevant marker on the map:

![image](https://user-images.githubusercontent.com/35113861/59159601-2b86fa00-8ac4-11e9-9821-23d6f81d7962.png)

Throughout the whole website I aimed for a simple and clean design. Utilising white space as much as possible and using only 3 colours consistently to result in a modern and uncluttered web app.


### Challenges and wins

There are two parts which I really enjoyed coding and saw it as great wins for me: searching and obtaining location details.

#### Searching

The SearchBar component took the users searchTerm, added it to a query string on the end of the Index component's URL and pushed the the app to that URL:

```
this.props.history.push('/entries?search='+this.state.searchTerm)
```

I then used the query-string module for Node to parse the query string stored in the props object of the component, into an object. The value of the of the search key of that object is then used to filter all the entries in the data base to only return the ones that match the searchTerm in their location, description or title fields:

```
filterEntries(){
  //Gets search props, parses into object and creates RegExp======================================
  const search = qs.parse(this.props.location.search).search
  const reSearch = new RegExp(search, 'i')
  const reWholeSearch = new RegExp('\\b'+search+'\\b', 'i')

  //Filters Entries based on seacrh and filter terms===============================================
  return this.state.entries.filter(entry =>
    (reSearch.test(entry.title) || reWholeSearch.test(entry.description) || reWholeSearch.test(entry.location))
  )
}
```

The filtering by category followed the same logic as above using query strings and the props object. Including category filter, now changed the above code to:

```
filterEntries(){
  //Gets search props, parses into object and creates RegExp======================================
  const search = qs.parse(this.props.location.search).search
  const reSearch = new RegExp(search, 'i')
  const reWholeSearch = new RegExp('\\b'+search+'\\b', 'i')

  const filterCategory = qs.parse(this.props.location.search).filtercategory
  const reFilterCategory = new RegExp(filterCategory, 'i')

  //Filters Entries based on seacrh and filter terms===============================================
  return this.state.entries.filter(entry =>
    (reSearch.test(entry.title) || reWholeSearch.test(entry.description) || reWholeSearch.test(entry.location))
    && reFilterCategory.test(entry.category.name)
  )
}
```

I realised that if the user filtered from the CategoryFilterBar, the component would push to a new URL that included only the CategoryFilterBar query string, regardless of if there was already a query string in place. I wanted the new filter to be added to the existing query string and include the searchTerm that was already there.

I therefore included code, that on submit of the SearchBar component and the CategoryFilterBar component checked to see if there was already a query string in the props object of the component and constructed the URL appropriately:

```
//Obtains current search prop and constructs the URL appropriately before re-direct.
handleSubmit(e){
  e.preventDefault()

  const searchProp = qs.parse(this.props.location.search)

  if (!Object.keys(searchProp).includes('filtercategory')){
    this.props.history.push('/entries?search='+this.state.searchTerm)
  } else {
    this.props.history.push('/entries?filtercategory='+searchProp.filtercategory+'&search='+this.state.searchTerm)
  }
}
```

The above is the conditional URL construction for the SearchBar. Corresponding conditional construction can be seen in the CategoryFilterBar component.

#### Location Details

AsyncSelect from ReactSelect was used to enable users to enter the name of the nearest town for their entry.

The drop down list of location options based on their input was populated via a Google Places API Autocomplete request. To avoid CORS (Cross-Origin Resource Sharing) issues a this request was send from the front end via an axios request to a route in the backend:

```
//Get the location options from Google Places API based on user input to react select==================================================================================
getLocationOptions (searchTerm) {
  return axios.get('/api/locations/'+searchTerm)
    .then(res => {
      return res.data.predictions.map(prediction => {
        return { value: prediction.description, label: prediction.description, location_id: prediction.place_id }
      })
    })
}
```

The Python Requests library was then used to make the requests to the Google API to get the location suggestions.

```
@router.route('/locations/<string:location>', methods=['GET'])
@db_session
def index(location):
    req = requests.get('https://maps.googleapis.com/maps/api/place/autocomplete/json',
        params={
            'key': google_geo_key,
            'input':location
            }
    )

    return jsonify(req.json())
```

Once the user selected the location they wanted a similar chain of events occured to get the details requireed details based on the place_id of the location from the Google Places API.

```
@router.route('/locations/details/<string:location_id>', methods=['GET'])
@db_session
def gps(location_id):
    req = requests.get('https://maps.googleapis.com/maps/api/place/details/json',
        params={
            'key': google_geo_key,
            'placeid':location_id
            }
    )

    return jsonify(req.json())
```

```
updateLocation(location) {
  axios.get('api/locations/details/'+location.location_id)
    .then(res => {

      const geoCords = res.data.result.geometry.location

      function checkComponent(component){
        return component.types.includes('administrative_area_level_1')
      }

      const stateName = res.data.result.address_components.filter(checkComponent)[0].long_name

      function matchState(state){
        return state.name === stateName
      }

      const stateId = this.state.states.filter(matchState)[0].id

      const data = {
        ...this.state.data,
        location: location.value,
        state_id: stateId,
        lat: geoCords.lat,
        lng: geoCords.lng
      }
      this.setState( {data} )
    })
}
```




## Future features
_If you were to revisit this project in the future what features would you add?_

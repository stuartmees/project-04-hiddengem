import React from 'react'
import axios from 'axios'
import Select from 'react-select'
import AsyncSelect from 'react-select/async'

const options = [
  { value: 1, label: 'Sleeping' },
  { value: 2, label: 'Eating' },
  { value: 3, label: 'Going' },
  { value: 4, label: 'Doing' }
]

class EntriesNew extends React.Component {
  constructor() {
    super()

    this.state = {
      data: {
        location: null
      }
    }

    this.updateLocation=this.updateLocation.bind(this)
    this.handleChange=this.handleChange.bind(this)
    this.handleCategoryChange=this.handleCategoryChange.bind(this)
    this.getLocationOptions=this.getLocationOptions.bind(this)
  }

  //Sets all other inputs values to state
  handleChange(e) {
    const data = { ...this.state.data, [e.target.name]: e.target.value }
    this.setState( {data} )
  }

  //Sets the selected category's id to state==========================================
  handleCategoryChange(selectedCategory) {
    const data = { ...this.state.data, category_id: selectedCategory.value}
    // this.setState({ data: {category_id: selectedCategory.value}
    this.setState( {data} )
    console.log('Category selected:', selectedCategory)
  }

  //Get the location options from Google Places API based on user input to react select==================================================================================
  getLocationOptions (searchTerm) {
    return axios.get('api/entries/locations/'+searchTerm)
      .then(res => {
        return res.data.predictions.map(prediction => {
          return { value: prediction.description, label: prediction.description, location_id: prediction.place_id }
        })
      })
  }

  //sets the seleted location to state.
  updateLocation(location) {
    axios.get('api/entries/location/gps/'+location.location_id)
      .then(res => {
        const gps = res.data.result.geometry.location
        const data = {...this.state.data, location: location.value, lat: gps.lat, lng: gps.lng}
        this.setState( {data} )
      })
  }

  //Makes the HTTP request to API using the state.data as the body of the request.
  handleSubmit(e) {
    e.preventDefault()

    axios.post('/api/entries/new', this.state.data)
      .then(this.props.history.push('/entries'))
      .catch(() => this.setState({ error: 'Invalid credentials' }))
  }

  componentDidMount() {
  }

  render() {
    const { category } = this.state.data

    console.log(location)
    return(
      <form>
        <div>
          <label>Category</label>
          <Select
            options={options}
            value={category}
            name='category_id'
            onChange={this.handleCategoryChange}
          />
        </div>

        <div>
          <label>Title</label>
          <input
            placeholder="Main tag line!"
            name="title"
            onChange={this.handleChange}
          />
        </div>

        <div>
          <label>Description</label>
          <input
            placeholder="josephine@bloggs.com"
            name="email"
            onChange={this.handleChange}
          />
        </div>

        <div>
          <label>Website</label>
          <input
            placeholder="www.greatplace.com"
            name="website"
            onChange={this.handleChange}
          />
        </div>

        <div>
          <AsyncSelect
            name="location"
            loadOptions={this.getLocationOptions}
            onChange={this.updateLocation}
          />
        </div>
      </form>
    )
  }
}

export default EntriesNew

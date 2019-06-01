import React from 'react'
import axios from 'axios'
import Select from 'react-select'
import AsyncSelect from 'react-select/async'
import ReactFilestack from 'filestack-react'

const categoryOptions = [
  { value: 1, label: 'Sleeping' },
  { value: 2, label: 'Eating' },
  { value: 3, label: 'Going' },
  { value: 4, label: 'Doing' }
]

const options = {
  accept: 'image/*'
  // transformations: {
  //   crop: true,
  //   circle: true,
  //   rotate: true
  // }
}

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
    this.handleSubmit=this.handleSubmit.bind(this)
    this.handleCategoryChange=this.handleCategoryChange.bind(this)
    this.getLocationOptions=this.getLocationOptions.bind(this)
  }

  //Sets all other inputs values to state
  handleChange(e) {
    const data = { ...this.state.data, [e.target.name]: e.target.value }
    this.setState( {data} )
  }

  //Sets the selected category's id to state==============================================
  handleCategoryChange(selectedCategory) {
    const data = { ...this.state.data, category_id: selectedCategory.value}
    // this.setState({ data: {category_id: selectedCategory.value}
    this.setState( {data} )
    console.log('Category selected:', selectedCategory)
  }

  //Get the location options from Google Places API based on user input to react select==================================================================================
  getLocationOptions (searchTerm) {
    return axios.get('/api/locations/'+searchTerm)
      .then(res => {
        return res.data.predictions.map(prediction => {
          return { value: prediction.description, label: prediction.description, location_id: prediction.place_id }
        })
      })
  }

  //sets the seleted location, state_id, lat and long to state=================================================================================
  updateLocation(location) {
    axios.get('api/locations/details/'+location.location_id)
      .then(res => {
        console.log(res.data.result.geometry)

        const geoCords = res.data.result.geometry.location

        function checkComponent(component){
          return component.types.includes('administrative_area_level_1')
        }

        console.log(res.data.result)

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

  handleUploadImages(result) {
    const data = { ...this.state.data, photo: result.filesUploaded[0].url}
    this.setState({ data })
    // toast.success('New Profile Image Updated!', {containerId: 'B'})
  }

  //Makes the HTTP request to API using the state.data as the body of the request=============
  handleSubmit(e) {
    e.preventDefault()

    axios.post('/api/entries', this.state.data)
      .then(this.props.history.push('/entries'))
      .catch(() => this.setState({ error: 'Invalid credentials' }))
  }

  //Gets the states from States model one mount
  componentDidMount() {
    axios.get('/api/states')
      .then(res => this.setState({states: res.data}))
  }

  render() {
    const { category } = this.state.data

    console.log(location)
    return(
      <div className="container-form">
          <form onSubmit={this.handleSubmit}>
            <div className="field">
              <label className="label">Category</label>
              <div className="control">
                <Select
                  options={categoryOptions}
                  value={category}
                  name='category_id'
                  onChange={this.handleCategoryChange}
                />
              </div>
            </div>

            <div className="field">
              <label className="label">Title</label>
              <div className="control">
                <input
                  className="input"
                  placeholder="Main tag line!"
                  name="title"
                  onChange={this.handleChange}
                />
              </div>
            </div>

            <div className="field">
              <label className="label">Description</label>
              <div className="control">
                <textarea
                  className="input"
                  placeholder="What's the deal with this place? What did you love? any tips?"
                  name="description"
                  onChange={this.handleChange}
                />
              </div>
            </div>


            <div className="field">
              <label  className="label">Website</label>
              <div className="control">
                <input
                  className="input"
                  placeholder="www.greatplace.com"
                  name="website"
                  onChange={this.handleChange}
                />
              </div>
            </div>

            <div className="field">
              <label className="label">Location</label>
              <AsyncSelect
                name="location"
                loadOptions={this.getLocationOptions}
                onChange={this.updateLocation}
              />
            </div>

            <div className="field">
              <label className="label">Photo</label>
              <div className="control">
                <ReactFilestack
                  apikey={process.env.FILESTACK_KEY}
                  buttonText="Upload Photo"
                  className="button"
                  options={options}
                  onSuccess={(result) => this.handleUploadImages(result)}
                  preload={true}
                />
              </div>
              {this.state.data.photo && <img src={this.state.data.photo} />}
            </div>

            <button className="button">Submit</button>
          </form>
        </div>
    )
  }
}

export default EntriesNew

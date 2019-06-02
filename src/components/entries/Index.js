import React from 'react'
import { Link, withRouter } from 'react-router-dom'
import axios from 'axios'
import ReactMapboxGl, { Popup, Marker } from 'react-mapbox-gl'
import qs from 'query-string'
import SearchBar from '../common/SearchBar'

const Map = ReactMapboxGl({
  accessToken: process.env.MAPBOX_ACCESS_TOKEN
})

class EntriesIndex extends React.Component {
  constructor(){
    super()

    this.state= null

    this.popUpShow = this.popUpShow.bind(this)
    this.popUpHide = this.popUpHide.bind(this)
  }

  filterEntries(){
    const re = new RegExp(qs.parse(this.props.location.search).search, 'i',)
    console.log(re)
    // const whole = new RegExp('\b'+qs.parse(this.props.location.search).search+'\b', 'i',)
    console.log(new RegExp('b'+qs.parse(this.props.location.search).search, 'i'))
    return this.state.entries.filter(entry => re.test(entry.title))
  }

  componentDidMount() {
    axios.get('/api/entries')
      .then(res => this.setState({ entries: res.data }))
  }

  popUpShow(entry) {
    this.setState({popup: { ...entry }})
  }

  popUpHide() {
    this.setState({popup: null})
  }

  render() {
    if(this.props.location.search) console.log(qs.parse(this.props.location.search))

    if(!this.state) return <p>Loading...</p>

    return(
      <div>
        <div className="container-map-search">
          <SearchBar />
        </div>

        <Map
          style="mapbox://styles/mapbox/streets-v9"
          center={[78.848090, 20.551730]}
          zoom={[4]}
          onClick={this.popUpHide}
          containerStyle={{
            height: '100vh',
            width: '100vw'
          }}>

          {this.state.popup &&
            <Link to={`/entries/${this.state.popup.id}`} key={this.state.popup.id}>
              <Popup
                coordinates={[this.state.popup.lng, this.state.popup.lat]}
                offset={{'bottom-left': [12, -38],  'bottom': [0, -38], 'bottom-right': [-12, -38]}}>
                <h1>{this.state.popup.title}</h1>
              </Popup>
            </Link>
          }

          {this.filterEntries().map(entry =>
            <div key={entry.id}>
              <Marker
                onClick={() => this.popUpShow(entry)}
                coordinates={[entry.lng, entry.lat]}
                anchor="bottom">
                <img src={'../../assets/marker.png'}/>
              </Marker>
            </div>
          )}

        </Map>
      </div>
    )
  }
}

export default EntriesIndex

// {this.state.entries.map(entry =>
//
// )}

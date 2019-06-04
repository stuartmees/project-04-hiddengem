import React from 'react'
import { Link, withRouter } from 'react-router-dom'
import axios from 'axios'
import ReactMapboxGl, { Popup, Marker } from 'react-mapbox-gl'
import qs from 'query-string'
import SearchBar from '../common/SearchBar'
import CategoryFilterBar from '../common/CategoryFilterBar'

const Map = ReactMapboxGl({
  accessToken: process.env.MAPBOX_ACCESS_TOKEN
})

const popUpStyles= {
  zIndex: '5'
}

class EntriesIndex extends React.Component {
  constructor(){
    super()

    this.state= null

    this.popUpShow = this.popUpShow.bind(this)
    this.popUpHide = this.popUpHide.bind(this)
  }

  filterEntries(){
    const search = qs.parse(this.props.location.search).search
    const reSearch = new RegExp(search, 'i')
    const reWholeSearch = new RegExp('\\b'+search+'\\b', 'i')

    const filterCategory = qs.parse(this.props.location.search).filtercategory
    const reFilterCategory = new RegExp(filterCategory, 'i')

    return this.state.entries.filter(entry =>
      (reSearch.test(entry.title) || reWholeSearch.test(entry.description) || reWholeSearch.test(entry.location))
      && reFilterCategory.test(entry.category.name)
    )
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

        <div className="map-filters">
          <div className="columns">
            <div className="column is-one-quarter">
              <SearchBar />
            </div>
            <div className="column is-one-quarter">
              <CategoryFilterBar />
            </div>
          </div>
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
                offset={{'bottom-left': [12, -38],  'bottom': [0, -38], 'bottom-right': [-12, -38]}}
                style={popUpStyles}
              >
                <div className="columns">
                  <div className="column">
                    <img src={this.state.popup.photo}/>
                  </div>
                  <div className="column">
                    <p>{`"${this.state.popup.title}"`}</p>
                  </div>
                </div>
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

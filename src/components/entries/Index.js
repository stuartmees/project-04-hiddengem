import React from 'react'
import axios from 'axios'
import ReactMapboxGl, { Marker } from 'react-mapbox-gl'

const Map = ReactMapboxGl({
  accessToken: process.env.MAPBOX_ACCESS_TOKEN
})

class EntriesIndex extends React.Component {

  componentDidMount() {
    axios.get('/api/entries')
      .then(res => this.setState({ entries: res.data }))
  }

  render() {
    if(!this.state) return <p>Loading...</p>

    return(
      <div>
        <Map
          style="mapbox://styles/mapbox/streets-v9"
          center={[78.848090, 20.551730]}
          zoom={[4]}
          containerStyle={{
            height: '100vh',
            width: '100vw'
          }}>

          {this.state.entries.map(entry =>
            <Marker key={entry.id}
              coordinates={[entry.lng, entry.lat]}
              anchor="bottom">
              <img src={'../../assets/marker.png'}/>
            </Marker>
          )}
        </Map>
      </div>
    )
  }
}

export default EntriesIndex

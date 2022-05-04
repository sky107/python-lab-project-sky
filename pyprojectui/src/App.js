import "./App.css";

import React, { Component } from "react";
import { Button, InputNumber, ButtonGroup, ButtonToolbar } from "rsuite";
import axios from 'axios';
import { Map, InfoWindow,  GoogleApiWrapper, Circle } from "google-maps-react";
import { Marker } from '@react-google-maps/api';
class App extends Component {
  constructor(props) {
    super(props);
    this.state = { data: [],range:0,type:false, userCoordinates:{lat:23.1455,lng: 75.7937},responseTime:0 };
  }

  componentDidMount(){
    axios.get(`https://python-project-sky.herokuapp.com/approach${this.state.type ? 1 : 2}?radius=${this.state.range}&lat=${this.state.userCoordinates.lat}&lng=${this.state.userCoordinates.lng}`)
    .then(res=>{
      console.log(res.data.data);
      this.setState({...this.state,data:res.data.data})
    })
    .catch(console.error)
  }

  handleChange(e=this.state.range){
    const beforeTime=new Date().getTime();
    axios.get(`https://python-project-sky.herokuapp.com/approach${this.state.type ? 1 : 2}?radius=${e}&lat=${this.state.userCoordinates.lat}&lng=${this.state.userCoordinates.lng}`)
    .then(res=>{
      const afterTime=new Date().getTime();
      const responseTime=afterTime-beforeTime;
      this.setState({...this.state,data:res.data.data,range:e,responseTime:responseTime})
    })
    .catch(console.error)
  }


   
  





  render() {
    return (
      <div className="App">
        {/* <h1>Google Maps in ReactJS - <small>Siddharth Kumar Yadav</small></h1> */}
        <div className="filter-container">
        
        <InputNumber
        // value={this.state.range}
        onChange={e=>{
          // this.setState({...this.state,range:e})
          this.handleChange(e)
        }}
          type="number"
          size="sm"
          min={0}
          style={{width:300}}
           placeholder="Enter Range in Kms " />
           <ButtonGroup
           size="sm"
           >
           {/* <Button color="green" appearance="primary">Draw</Button> */}
        <Button appearance={this.state.type === false ? "primary" : "ghost"} color="green"  onClick={()=>this.setState({...this.state,type:!this.state.type})}>GeoSpatial Queries</Button>
        </ButtonGroup>
        <div>
        <small>Response Time : {this.state.responseTime} ms</small>
        </div>
        </div>
        <Map
          google={this.props.google}
          initialCenter={{
            lat: 23.1455,
            lng: 75.7937,
          }}
          default
          zoom={10}
        >

          <Circle
          center={{lat:this.state.userCoordinates.lat,lng:this.state.userCoordinates.lng}}
          options={ {
            strokeColor: '#FF0000',
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: '',
            fillOpacity: 0.35,
            clickable: false,
            draggable: false,
            editable: false,
            visible: true,
            radius: 30000,
            zIndex: 1
          }}

          radius={1000*(this.state.range)}



          
            />
          <Marker
          key="user-location"
              position={{lat:this.state.userCoordinates.lat,lng:this.state.userCoordinates.lng}}
              draggable
              name={"Current location"}
              onDragEnd={e=>
                {
                  console.log(e.latLng.lat())
                  console.log(e.latLng.lng())
                  this.setState({...this.state,userCoordinates:{lat:e.latLng.lat(),lng:e.latLng.lng()}})
                }
              
              }
            />
          
          {/* {
            [{lat:12,lng:12}].map(e=>{
              return <Marker
              key={'sdf '}
              postition={{lat:e.lat,lng:e.lng}}
              />
            })
          } */}
          {this.state.data?.map((e,idx)=>{
            console.log("E",e)
              return <Marker
              key={`store-${idx}`}
              position={{lat:parseFloat(e.location.coordinates[0]),lng:parseFloat(e.location.coordinates[1])}}
              // draggable
              icon={'http://www.google.com/intl/en_us/mapfiles/ms/micons/blue-dot.png'}
              name={"Current location"}
            />
          })}
          
        </Map>
      </div>
    );
  }
}

export default GoogleApiWrapper({
  apiKey: "AIzaSyBkoquOdohlv2AB9RisuEgPQajwbZIhMNQ",
})(App);

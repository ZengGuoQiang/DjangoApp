import React, { Component } from 'react';
import axios from 'axios';
import './App.css';

axios.defaults.withCredentials = true;
axios.defaults.headers.post['Content-Type'] = 'application/json';
const server = 'http://127.0.0.1:8000';

class App extends Component {
  constructor (props) {
    super(props);
    this.state = {
      name: "",
      age: 0,
      data:""
    }
    this.change = this.change.bind(this);
    this.write = this.write.bind(this);
    this.read = this.read.bind(this);
  }

  change(key, e) {
    this.setState({
      [key]: e.target.value
    });
  }

  async write() {
    let data = this.state ;
    let res = await axios({
                            method: 'POST',
                            url: 'http://127.0.0.1:8000/write/',
                            data: data,
                            headers: {
                                'Content-type': 'application/x-www-form-urlencoded'
                            }
                        });

    console.log(data);
    console.log(res);
  }

  async read() {
    let params = {
      name:'1'
    }
    // let res = await axios.get(`/api/read/`, { paramas });
    let res = await axios({
                          method: 'GET',
                          url: 'http://127.0.0.1:8000/read/',
                          data: params,
                          headers: {
                            'Content-type': 'application/json'
                          }
    });
    console.log(res)
  }
  componentWillMount() {
    console.log(1)
  }
  componentDidMount() {
   var res =  axios({
        method: 'GET',
        url: 'http://127.0.0.1:8000/getCode/',
        async:false,
        headers: {
          'Content-type': 'application/json'
        },
        success: function (res) {
                  console.log(res)    
                  this.setState({ "data": res })     
        }
    });
    console.log(res)
    console.log(2)
  }
  render() {
    return (
      <div className="App">
        <input onChange={ (e) => (this.change('name', e)) } />
        <br />
        <input onChange={ (e) => (this.change('age', e)) } />
        <br />
        <button onClick={ this.write }>write</button>
        <button onClick={ this.read }>read</button>
        {/* <ul>
          {
            this.state.data.map((item, i) => {
              return <li key={ i}>{ item}</li>
            })
          }
        </ul> */}
      </div>
    );
  }
}

export default App;

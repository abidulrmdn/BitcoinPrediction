import React, { Component } from 'react';
import logo from './bitcoin_1.png';
import loadingImage from './bitcoin-animation-6.gif';
import btcdown from './bitcoin-down.png';
import btcup from './bitcoin-up.png';
import btcerror from './bitcoin-error.png';
import './App.css';

class App extends Component {
  render() {
      return (
        <div className="App">
            <ParametersForm />
        </div>
      );
  }
}

class ParametersForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {value: '', prediction: [], isLoading: false, isError: false};

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }

    handleSubmit(event) {
        this.setState({
            isLoading: true,
            prediction: [],
            isError: false
        }, function(){

        });

        console.log('A hashtag was submitted: ' + this.state.value);
        event.preventDefault();
        let fetchUrl = "";
        if(this.state.value === 'dummy-error') {
          fetchUrl = process.env.PUBLIC_URL + '/dummy-prediction-error.json?v=' + this.state.value;
        } else if(this.state.value === 'dummy-no') {
          fetchUrl = process.env.PUBLIC_URL + '/dummy-prediction-dont-buy.json?v=' + this.state.value;
        } else if(this.state.value === 'dummy-buy') {
          fetchUrl = process.env.PUBLIC_URL + '/dummy-prediction-buy-now.json?v=' + this.state.value;
        } else {
          fetchUrl = 'http://localhost:8001/api/prediction/' + this.state.value;
        }
        console.log("fetchUrl");
        console.log(fetchUrl);
        fetch(fetchUrl)
            .then((resp) => resp.json())
            .then(json => {
              console.log("we got successful msg for the JSON", json);
              this.setState({
                  prediction: json,
                  isLoading: false,
                  isError: false
              });
            })
            .catch(err => {
              console.log("we got error for the JSON", err);
              this.setState({
                  isLoading: false,
                  isError: true
              });
              console.error(this.props.url, err.toString())
            })
    }

    render() {
        console.log("this.state.prediction");
        console.log(this.state.prediction);
        console.log("this.state.prediction.data");
        console.log(this.state.prediction.data);
        let loadingAnimation = <img id="mainImage" alt="logo" src={logo} />;
        if (this.state.isLoading) {
            console.log("this.state.prediction-1");
            loadingAnimation = <img id="mainImage" alt="loading" src={loadingImage} />
        } else if (this.state.isError) {
            console.log("this.state.prediction-2");
            loadingAnimation = <img id="mainImage" alt="error!" src={btcerror} />
        } else if (this.state.prediction){
            console.log("this.state.prediction-5");
            console.log(this.state.prediction);
            if( this.state.prediction.data == 0) {
               console.log("this.state.prediction-3");
                loadingAnimation = <img id="mainImage" alt="it goes down" src={btcdown} />
            } else if (this.state.prediction.data == 1) {
                console.log("this.state.prediction-4");
                loadingAnimation = <img id="mainImage" alt="it goes up" src={btcup} />
            }
        }

        return (
        <div id="layout-content" className="layout-content-wrapper">
            <header className="App-header">
                {loadingAnimation}
            </header>
            <br />
            <form onSubmit={this.handleSubmit}>
                <label>
                    <input className="hashtag-input" type="text" value={this.state.value} onChange={this.handleChange} placeholder="Enter a hashtag to predict, e.g. #trump" />
                </label>
                <input className="hashtag-submit" type="submit" value="Submit" />
            </form>
        </div>
        );
    }
}

export default App;

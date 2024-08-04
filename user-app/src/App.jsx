import React from 'react';
import DataTable from './DataTable';
import { Header } from './Header';
import Form from './Form';
import logo from './assets/logo.png'
import './App.css';


const data = 
  [{
    "name": "Adeel Solangi",
    "language": "Sindhi",
    "bio": "Donec lobortis eleifend condimentum. Cras dictum dolor lacinia .ecenas quis nisi nunc.",
    "version": 6.1
},
{
    "name": "Afzal Ghaffar",
    "language": "Sindhi",
    "bio": "Aliquam sollicitudin ante ligula, eget malesuada nibh efficitur et.",
    "version": 1.88
},
{
    "name": "Aamir Solangi",
    "language": "Sindhi",
    "bio": "Vestibulum pharetra libero et velit gravida euismod. Fusce eu ultrices elit.",
    "version": 7.27
},
{
    "name": "Abla Dilmurat",
    "language": "Uyghur",
    "bio": "Donec lobortis eleifend condimentum. Morbi ac tellus erat.",
    "version": 2.53
}]

function App() {
    return (
      <div className="container">
        <div className="row">
          <div className="col-lg-12">
              <Header />
              </div>
             </div>
             <div className='row'>
                <div className='col-lg-12 pb-5'>
                  <DataTable data={data} />
            </div>
          </div>
         {/* <Form />  */}
        </div>

     






      
    );
}

export default App;



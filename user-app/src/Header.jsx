import React, { useState } from 'react';
import './App.css';
import logo from './assets/logo.png'
import handleForm from './Form';
import Modal from './Modal';


export const Header = () => {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <header className="text-white p-5">
        <div className="flex justify-between items-center px-5 mt-3 py-8">
          <div className="text-lg font-bold">
            <img src={logo} className='h-10 w-auto' alt="Logo"/>
          </div>
          <div>
            <button 
              className='px-4 py-2 bg-blue-500 hover:bg-blue-700 rounded' 
              onClick={() => setShowModal(true)}
            >
              Create
            </button>
            <button className='px-4 py-2 bg-red-500 hover:bg-red-700 rounded ml-4' onClick={handleForm}>Log out</button>
          </div>
        </div>
      </header>
      <Modal showModal={showModal} setShowModal={setShowModal} />
    </>
  )
}

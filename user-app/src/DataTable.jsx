import React from 'react';
import './App.css';

const DataTable = ({ data }) => {
    return (
        <div className="container py-4 px-5">
            <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                <thead className="text-xs text-slate-300 uppercase bg-gray-50 dark:bg-gray-300 dark:text-gray-400">
                    <tr>
                        <th scope="col" className="px-6 py-3 text-start text-sm font-bold text-black uppercase">Name</th>
                        <th scope="col" className="px-6 py-3 text-start text-sm font-bold text-black uppercase">Language</th>
                        <th scope="col" className="px-6 py-3 text-start text-sm font-bold text-black uppercase">Bio</th>
                        <th scope="col" className="px-6 py-3 text-start text-sm font-bold text-black uppercase">Version</th>
                        <th scope="col" className="px-6 py-3 text-end text-sm font-bold text-black uppercase">Action</th>
                    </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                    {data.map((item) => (
                        <tr key={item.id} className='odd:bg-white odd:dark:bg-gray-100 even:bg-gray-50 even:dark:bg-gray-300'>
                            <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-800">{item.name}</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-800">{item.language}</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-800">{item.bio}</td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-800">{item.version}</td>
                            <td className="px-6 py-4 whitespace-nowrap text-end text-sm font-medium relative">
                                <div className="dropdown inline-block relative pb-5 cursor-pointer group">
                                    <span className="text-gray-800 text-2xl inline-block">⋮</span>
                                    <div className="dropdown-content absolute right-0 mt-2 w-28 bg-white border border-gray-200 rounded shadow-lg opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                                        <a href="#" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Edit</a>
                                        <a href="#" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100">Delete</a>
                                    </div>
                                </div>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default DataTable;

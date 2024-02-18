import "../styles/search.css"
import Logo from "../assets/koiZen.svg"
import React, { useEffect } from 'react'
import { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faMagnifyingGlass } from '@fortawesome/free-solid-svg-icons'
import { motion, useAnimationControls } from "framer-motion";


function Search() {

    const [firstName, setFirstName] = useState('');
    // const [age, setAge] = useState('20');
    // const ageAsNumber = Number(age);


    return (
        <div className="search">
            <img className="zen-icon" src={Logo} alt="logo" />
            <motion.div whileHover={{ scale: 1.2 }} >
                <label className="search-area">
                    <FontAwesomeIcon icon={faMagnifyingGlass} />
                    <input className="search-bar" value={firstName} onChange={e => setFirstName(e.target.value)} />
                </label>
            </motion.div>
            <div>
                {firstName !== '' && <p>Your Query: {firstName}</p>}
            </div>

        </div>

    );
}

export default Search;

// import { useState } from 'react';

// export default function Form() {
//     const [firstName, setFirstName] = useState('');
//     const [age, setAge] = useState('20');
//     const ageAsNumber = Number(age);
//     return (
//         <>
//             <label>
//                 First name:
//                 <input value={firstName} onChange={e => setFirstName(e.target.value)} />
//             </label>
//             <label>
//                 Age:
//                 <input value={age} onChange={e => setAge(e.target.value)} type="number" />
//                 <button onClick={() => setAge(ageAsNumber + 10)}> Add 10 years </button>
//             </label>
//             {firstName !== '' && <p>Your name is {firstName}.</p>
//             }
//             {ageAsNumber > 0 &&<p>Your age is {ageAsNumber}.</p>
//             }
//         </>
//     );
// }

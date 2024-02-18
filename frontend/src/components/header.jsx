import "../styles/header.css"

import React, { useEffect } from 'react'
import { useState } from 'react';


function Header() {
    //funcs and consts go here

    return (
        <div className="header">
            <div className="header-card">
                <h1>Koi</h1>
                <h2>Common Carp Breed</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras porta enim ut justo varius, eu volutpat dui vulputate. Ut fringilla lectus leo, pulvinar blandit augue iaculis nec. Fusce sollicitudin arcu et elit consequat venenatis. Aliquam nec scelerisque neque, in fermentum felis. Nullam aliquam odio vel sapien lacinia, eu lacinia ligula tempus. Integer sit amet auctor purus, tristique sodales eros. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Interdum et malesuada fames ac ante ipsum primis in faucibus.

                    Sed dapibus massa vel odio imperdiet, id sodales nunc tristique. Curabitur sollicitudin luctus mollis. Phasellus arcu elit, facilisis eget rhoncus vel, accumsan sit amet nisi. Nulla in vestibulum neque, non ultrices arcu. Vivamus interdum pulvinar mauris vitae porttitor. Fusce nec tincidunt dolor, sollicitudin sagittis libero. Aliquam vitae ex elementum, tempor elit at, tincidunt sapien. Curabitur in vestibulum risus. Integer eget purus fermentum, eleifend est eu, lobortis sapien. Maecenas pellentesque risus purus, vitae accumsan lorem gravida eget. Duis vel tellus lacus. Praesent vulputate nec tellus in pellentesque.</p>
            </div>
        </div>

    );
}

export default Header;

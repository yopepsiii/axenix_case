import Logo from "../logo/Logo"
import Search from "../search/Search"
import "./Header.css"

export default function Header(){
    return(
        <header>
            <Logo></Logo>
            <Search/>
        </header>
    )
}
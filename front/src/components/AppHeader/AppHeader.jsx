import AppHeaderStyles from './AppHeader.module.css';

const AppHeader = () => {
    return (
        <header>
            <nav className={AppHeaderStyles.nav}>
                <p>Сет
                    Рюмочных
                </p>
                <p>Новости/Ивенты</p>
                <p>Меню</p>
                <p>Рюмочные</p>
                <p>Контакты</p>
                <p>О проекте</p>
            </nav>
            {/*<nav className={AppHeaderStyles.nav}>*/}
            {/*    <div className={`p-1 ${AppHeaderStyles.rowColumn}`}>*/}
            {/*        <BurgerIcon type="secondary"/>*/}
            {/*        <NavLink to='/'*/}
            {/*                 className={({isActive}) => `pl-3 mr-10 text text_type_main-default ${isActive ? '' : 'text_color_inactive'} ${AppHeaderStyles.link}`}>*/}
            {/*            Конструктор*/}
            {/*        </NavLink>*/}

            {/*        <ListIcon type="secondary"/>*/}

            {/*        <NavLink to='/profile/orders'*/}
            {/*                 className={({isActive}) => `pl-3 text text_type_main-default ${isActive ? '' : 'text_color_inactive'} ${AppHeaderStyles.link}`}>*/}
            {/*            Лента заказов*/}
            {/*        </NavLink>*/}
            {/*    </div>*/}
            {/*    <div className="p-1">*/}
            {/*        <Logo/>*/}
            {/*    </div>*/}
            {/*    <div className={`p-1 ${AppHeaderStyles.rowColumn}`}>*/}

            {/*        <ProfileIcon type="secondary"/>*/}

            {/*        <NavLink to='/profile'*/}
            {/*                 className={({isActive}) => `pl-3 text text_type_main-default ${isActive ? '' : 'text_color_inactive'} ${AppHeaderStyles.link}`}>*/}
            {/*            Личный кабинет*/}
            {/*        </NavLink>*/}
            {/*    </div>*/}
            {/*</nav>*/}
        </header>
    );
};

export default AppHeader;

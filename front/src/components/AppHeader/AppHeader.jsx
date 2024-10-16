import AppHeaderStyles from './AppHeader.module.css';

const AppHeader = () => {
    return (
        <header>
            <nav className={AppHeaderStyles.nav}>
                <img src="/logo.svg" alt="Логотип" />
                <div className={AppHeaderStyles.title}>
                    <p>Сет</p>
                    <p>Рюмочных</p>
                </div>

                <p>Новости/Ивенты</p>
                <p>Меню</p>
                <p>Рюмочные</p>
                <p>Контакты</p>
                <p>О проекте</p>
            </nav>
        </header>
    );
};

export default AppHeader;

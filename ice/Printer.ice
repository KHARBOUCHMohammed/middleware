module Demo
{
    sequence<byte> bytes;
    sequence<string> StringSeq;
    interface Printer
    {
        void printString(string s);
        int GetNumberOfMusics();
        StringSeq GetMusiques(int i);

        StringSeq SearchTitle(string title);
        StringSeq SearchArtist(string artist);

        void AjtMusique(int offset, bytes partiesMusique, string path, string titre, string artistes, string album);
        void AjtMusiqueDatabase(string titre, string artistes, string album);

        void ModifMusique(string musiqueAModifier, string nouveauTitre, string nouveauxArtistes, string nouvelAlbum);

        void DeleteMusic(string name);
        bool Play(string music);
        string Pause();
        bool Stop();

    }

    interface PrinterFactory
    {
        Printer* createPrinter();
    }
}